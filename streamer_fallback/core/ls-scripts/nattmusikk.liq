night_jingle = single("{{ liquidsoap.nightmusic.jingle }}")

nightmusic = playlist("{{ liquidsoap.nightmusic.directory }}")
nightmusic = rotate(weights=[1,1],[nightmusic, night_jingle])
nightmusic = normalize(nightmusic, gain_max=1000.0, target=-1.0, window=2.0)
nightmusic = nrj(nightmusic)
nightmusic = smart_crossfade(nightmusic)

output.icecast(
%mp3(stereo={{ icecast.format.stereo }}, samplerate={{ icecast.format.samplerate }}, bitrate={{ icecast.format.bitrate }}),
host = "{{ icecast.host }}", port = {{ icecast.port }},
password = "{{ icecast.source.password }}", mount = "{{ icecast.fallback_mount }}",
nightmusic)

