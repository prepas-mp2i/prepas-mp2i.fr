---
title: {{ replace .Name "-" " " | title }}
slug: {{ replace .Name "-" " " | urlize }}
date: {{ .Date }}
draft: false
---