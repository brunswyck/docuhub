*******
parsing
*******

cli options parsing
===================

code with cli parsing
---------------------

.. todo:: revise code

.. code-block:: python

   #!/usr/bin/env python3
   import os
   import re
   from youtube_search import YoutubeSearch
   import pprint
   import subprocess
   import ffmpeg
   from optparse import OptionParser
   import time
   pp = pprint.PrettyPrinter(indent=2)
   home = os.getenv('HOME')
   music_folder = os.path.join(home, "Music")
   yt_dl_proc = os.path.join(home, ".local/bin/youtube-dl")
   converted_folder = os.path.join(music_folder, "converted")
   
   
   def convert(song, wanted_format):
       song_name = song.rsplit('.', 1)[0]
       new_song_name = song_name + "." + wanted_format
       song_orig = os.path.join(music_folder, song)
       song_dest = os.path.join(converted_folder, new_song_name)
       pp.pprint(song_dest)
       if not os.path.exists(converted_folder):
           os.makedirs(converted_folder)
       (
           ffmpeg
           .input(song_orig)
           .output(song_dest, acodec=wanted_format, strict="experimental")
           .overwrite_output()
           .run(capture_stdout=True)
       )
   
   
   def strip_bad_chars(bad_string):
       # coding: utf8
       bad_chars = [';', ':', '!', '*', '$', ',', '(', ')', '&']
       for character in bad_chars:
           bad_string = bad_string.replace(character, '')
       # remove weird non string.printable utf-8 characters
       bad_string = re.sub(r'[^\x00-\x7f]', r'', bad_string)
       return bad_string
   
   
   def replace_unfriendly_chars(long_string):
       """
       1. strip youtube suffix
       2. replace spaces with underscores
       3. strip bad characters
       4. strip trailing chars
       5. strip repeating chars
       """
       operations = [strip_youtube_suffix, replace_spaces_with_underscores, strip_bad_chars, strip_trailing_chars,
                     strip_repeating_chars]
       for op in operations:
           long_string = op(long_string)
       return long_string
   
   
   def strip_trailing_chars(long_string):
       return re.sub(r'(\W|_)+(\.\w{3})', r'\2', long_string)
   
   
   def strip_repeating_chars(long_string):
       return re.sub(r'(\W|_){2,}', '_', long_string)
   
   
   def replace_spaces_with_underscores(long_string):
       return re.sub(r'\s', '_', long_string)
   
   
   def strip_youtube_suffix(from_string, length_suffix=11):
       youtube_pattern = r'(\W\w{' + re.escape(str(length_suffix)) + r'})(\.\w{3})'
       return re.sub(youtube_pattern, r'\2', from_string)  # replace group1, keep matched group2
   
   
   def loop_over_files_in(folder, apply_this_function):
       new_name = ""
       for file in os.listdir(folder):
           new_name = apply_this_function(file)  # todo: check if function returns string
           if new_name:
               os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
   
   
   def search_youtube(search_phrase):
       results = YoutubeSearch(search_phrase, max_results=10).to_json()
       return results
   
   
   def convert_audio(folder, format_to_convert, wanted_format):
       for file in os.listdir(folder):
           if file.endswith(format_to_convert):
               file_location = os.path.join(folder, file)
               print(file_location)
               # file_name = file.rsplit('.', 1)  # split only once
               # convert(file, this_format, to_that_format)
               # song = AudioSegment.from_file(file_location, current_format)               # song.export(file_location, wanted_format)
   
   
   def clean_audio_filenames():
       loop_over_files_in(music_folder, replace_unfriendly_chars)
   
   
   # https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme
   def download_youtube_audio(youtube_id, audio_format="opus"):
       title_args = [yt_dl_proc, "--get-title", youtube_id]
       yt_dl_args = [yt_dl_proc, "-x", "--audio-format", audio_format, "-o", "%(title)s.%(ext)s", youtube_id]
       # Specify audio format: "best", "aac", "flac", "mp3", "m4a", "opus", "vorbis", or "wav"; "best" by default; N
       # webm container on youtube has ogg audio = opus by default
       os.chdir(music_folder)
       try:
           pp.pprint("downloading " + youtube_id + " in " + str(audio_format) + " format")
           subprocess.run(args=yt_dl_args, check=True)
           # returns cleaned song_title = filename  # .strip() removes trailing \n
           song_title = subprocess.run(args=title_args, check=True, capture_output=True, text=True).stdout.strip()
           return replace_spaces_with_underscores(str(song_title) + "." + str(audio_format))
       except subprocess.CalledProcessError as proc_err:
           print("Failed to run youtube-dl with error: " + str(proc_err))
   
   
   def check_youtube_id(yt_id):
       id_pattern = r'\w{11}'
       result = re.match(id_pattern, yt_id)
       if result and len(yt_id) == 11:
           return result
       else:
           raise Exception("youtube id has to be exactly 11 alphanumeric characters")
   
   # https://docs.python.org/3/library/optparse.html
   def main():
       usage = "usage: %prog [options] youtube_id"
       parser = OptionParser()
       # parser.add_option("-i", "--input", dest="input_format", help="audio format as input, eg: ogg", metavar="INPUT")
       parser.add_option("-o", "--out-format", dest="output_format", default="opus",
                         help="Specify audio format: \"best\", \"aac\", \"flac\", \"mp3\", \"m4a\","
                              " \"opus\", \"vorbis\", \"wav\" \"best\"",
                         metavar="OUTPUT")
       parser.add_option("-v", action="store_true", dest="verbose", default=True, help="let's hear it!")
       parser.add_option("-q", action="store_false", dest="verbose", help="hush little puppy :)")
       (options, args) = parser.parse_args()
       pp.pprint("options: " + str(options))
       pp.pprint("arguments: " + str(args))
       youtube_id = "Wa9YSAdbKh8"
       if len(args) < 1:
           raise Exception("youtube id argument required")
       elif len(args) > 1:
           raise Exception("only Youtube id required, don't specify additional arguments")
       elif check_youtube_id(args[0]):
           youtube_id = args[0]
       else:
           raise Exception("not a valid youtube id given as argument, pls double check")
       pp.pprint(search_youtube('binaural music focus'))
       wanted_format = 'mp3'
       song_downloaded = download_youtube_audio(youtube_id)
       # clean_audio_filenames()
       # time.sleep(10)
       # convert(song_downloaded, "m4a")
       test_song = "test_song.m4a"
       # convert(test_song, "m4a")
