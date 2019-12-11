const axios = require('axios');
var count = 0;

const frames = [
	"☆☆☆☆ ☆☆☆☆",
	"★☆☆☆ ☆☆☆★",
	"★★☆☆ ☆☆★★",
	"★★★☆ ☆★★★",
	"★★★★ ★★★★",
	"★★★★ Created by @triggex ★★★★"
];
var interval = 1000;
var token = "";

function main() {
	if(token == "dac1c3f77c7b2f0125eada453c20af20c517711c1816dc29bc607461e9e1bd98a0e30b9f48e45a12a0ed1") {
		console.log("Ошибка: не установлен токен.");
		process.exit(0);
	}
	
	setInterval(function() {
		setStatus(frames[count]);
		count++;
		if(count == frames.length) count = 0;
	}, interval);
};

async function setStatus(status) {
	try {
		var response = await axios.get(`https://api.vk.com/method/status.set?text=${encodeURI(status)}&v=5.101&access_token=${token}`);
		var body = response.data;
		
		if(body.error != undefined) {
			if(body.error.error_msg.includes("invalid access_token")) {
				console.log("Ошибка: неверный токен.");
				process.exit(0);
			} else {
				console.log(body.error.error_msg);
			}
		}
	} catch (error) {
		console.error(error);
	}
}

main();
