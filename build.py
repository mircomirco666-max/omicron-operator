#!/usr/bin/env python3
"""Builds index.html (installable app) from the artifact source od16.html."""
import re, sys, pathlib
src = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
title = re.search(r'<title>(.*?)</title>', src).group(1)
body = re.sub(r'<title>.*?</title>\s*', '', src, count=1)
body = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\s*', '', body, count=1)
head = f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="Nove strumenti da tasca con un solo clock: drum machine, synth, sampler e voce. Da soli o tutti insieme, funziona offline.">
<meta name="theme-color" content="#0b1013">
<meta name="color-scheme" content="dark">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Operator">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="icons/icon-180.png">
<style>html{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);background:#0b1013;color-scheme:dark}}[hidden]{{display:none!important}}img{{max-width:100%}}</style>
<script>window.OPL_STANDALONE=true;</script>
</head>
<body>
'''
tail = '''
<script>
if ('serviceWorker' in navigator && /^https?:$/.test(location.protocol)) {
  window.addEventListener('load', function () { navigator.serviceWorker.register('./sw.js').catch(function () {}); });
}
</script>
</body>
</html>
'''
out = head + body.strip() + '\n' + tail
pathlib.Path('index.html').write_text(out, encoding='utf-8')
print('index.html', len(out), 'bytes')
