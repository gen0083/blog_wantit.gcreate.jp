---
title: "{{ replace .Name "-" " " | title }}"
slug: {{ .Name }}
description:
{{ $parent_path := replaceRE ".*post/(.+?)/.*" "$1" .Path -}}
featuredimage: images/cover/{{ $parent_path }}.jpg
date: {{ .Date }}
tags:
    -
product:
    name:
    rate:
    link:
    comment:
    kaeyome:
    amazon:
    rakuten:
---

<!--more-->

##
