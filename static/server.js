var Gun = require("gun");
var server = require('http').createServer().listen(8765);
var gun = Gun({web: server});