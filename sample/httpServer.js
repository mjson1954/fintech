var http = require("http");

http.createServer(function (req, res) {
    console.log("요청이 발생하였습니다.");
	var body = "hello Server";
	res.setHeader('Content-Type', 'text/plain; charset=utf-8');
	res.end("안녕하세요!!!!!")
}).listen(3000);
