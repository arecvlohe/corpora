# -*- coding: utf-8 -*-


from corpora.utils.tmp_files import prepare_temporary_environment
from transcription.models import \
    TranscriptionSegment

from subprocess import Popen, PIPE

import logging
logger = logging.getLogger('corpora')


def dummy_segmenter(audio_file_path):
    MIN_DURATION = 4*100
    MAX_DURATION = 10*100

    code = "ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {0}".format(
        audio_file_path)

    p = Popen(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of',
         'default=noprint_wrappers=1:nokey=1', audio_file_path],
        stdin=PIPE, stdout=PIPE)

    output, errors = p.communicate()

    duration = float(output)*100  # Milliseconds
    logger.debug("DURATION: {0:.2f}".format(duration))
    logger.debug("SEGMENTS:\n")
    segments = []
    time = 0
    while (time + MAX_DURATION) < duration:
        dt = MAX_DURATION + time
        segments.append((time, dt))
        logger.debug("{0:04.2f}, {1:04.2f}".format(time, dt))
        time = time + MAX_DURATION

    segments.append((time, duration))

    if len(segments) > 1:
        last_chunk = segments[-1]
        if last_chunk[1] - last_chunk[0] < MIN_DURATION:
            segments.pop()
            segments.pop()
            segments.append((time-MAX_DURATION, duration))
        time, dt = segments[-1]
        logger.debug("{0:04.2f}, {1:04.2f}".format(time, dt))

    return segments


def create_transcription_segments_admin(aft):
    try:
        ts = create_and_return_transcription_segments(aft)
    except Exception as e:
        return "{0}".format(e)

    return "Created {0} segments from {1}".format(len(ts), aft.name)


def create_and_return_transcription_segments(aft):
    '''
    Creates the transcription segments from an AudioFileTranscription model.
    '''

    # We should delete all segments if we're going to create more!
    deleted = TranscriptionSegment.objects.filter(parent=aft).delete()

    try:
        file_path, tmp_stor_dir, tmp_file, absolute_directory = \
            prepare_temporary_environment(aft)
    except Exception as e:
        logger.debug('ERROR: {0}'.format(e))
        raise ValueError("{0}".format(e))

    segments = dummy_segmenter(tmp_file)

    ts_segments = []
    for segment in segments:

        start = segment[0]
        end = segment[1]

        ts, created = TranscriptionSegment.objects.get_or_create(
            start=start,
            end=end,
            parent=aft)

        ts_segments.append(ts)
    return ts_segments