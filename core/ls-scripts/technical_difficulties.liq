error = single("{{ liquidsoap.error.looping_jingle.path }}")
error = amplify({{ liquidsoap.error.looping_jingle.amplification_factor }}, error)

output.icecast(
%mp3(stereo={{ icecast.format.stereo }}, samplerate={{ icecast.format.samplerate }}, bitrate={{ icecast.format.bitrate }}),
host = "{{ icecast.host }}", port = {{ icecast.port }},
password = "{{ icecast.source.password }}", mount = "{{ icecast.fallback_mount }}",
error)

