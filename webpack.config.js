const path = require("path");

module.exports = [{
    entry: './src/app.scss',
    output: {
      // This is necessary for webpack to compile
      // But we never use style-bundle.js
      path: path.resolve(__dirname, "static"),
      filename: 'style-bundle.js',
    },
    module: {
      rules: [
        {
          test: /\.scss$/,
          use: [
            {
              loader: 'file-loader',
              options: {
                name: 'bundle.css',
              },
            },
            { loader: 'extract-loader' },
            { loader: 'css-loader' },
            { loader: 'sass-loader' },
          ]
        }
      ]
    },
  }];