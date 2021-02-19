const path = require("path");
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {
  entry: "./index.js",
  output: {
    path: path.resolve(__dirname, "../legal_db/static/webpack_files/js"),
    filename: "index.js",
  },
  module: {
    rules: [
      {
        test: /\.(scss)$/,
        use: [MiniCssExtractPlugin.loader,'css-loader','sass-loader'],
      },
    ],
  },
  plugins:[new MiniCssExtractPlugin({filename:'../css/index.css'})]
};
