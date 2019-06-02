#!/bin/sh

if [ "$#" -gt 0 ]
then
    opt="$1"
else
    opt="dev"
fi

echo $opt

npx uglifycss themes/aether/assets/css/*.css src/style.css > static/style.css

if [ $opt = "prod" ]
then
    npx postcss static/style.css -u autoprefixer -o static/style.css --no-map
else
    npx postcss static/style.css -u autoprefixer -o static/style.css
fi