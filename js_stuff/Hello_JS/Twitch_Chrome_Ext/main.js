const streamersArray = [
"ESL_SC2", "OgamingSC2", "freecodecamp", "syndicate", "riotgames", "esl_csgo", "nightblue3", "summit1g"
];
const baseTwitchUrl = 'https://www.twitch.tv/';

function requestStatusCheck(response) {
    if (response.status === 200) {
        return response;
    } else {
        throw new Error(response.statusText);
    }
}

async function getStreamMetadata(stream) {
    const baseUrl = 'https://wind-bow.gomix.me/twitch-api';
    const childStream = '/streams/';

    const request = await fetch(baseUrl+childStream+stream);
    requestStatusCheck(request);
    const obj = await request.json();
    return obj;
}

async function letsGo() {
    const streams = await Promise.all(streamersArray.map(getStreamMetadata));
    asyncFor(streams);

}

function asyncTimer(n, fn) {
    setTimeout(fn, n);
}


function asyncFor(myArray){

    let i = 0, length = myArray.length, fn = function() {
        if (i < length) {
            let currentJson = myArray[i];
            if (currentJson['stream'] === null) {
                const myElementName = myArray[i]['_links']['self'].match(/\/streams\/+([a-zA-Z0-9]*)/);
                const node = document.createElement('div');
                const nodeLink = document.createElement('a');
                node.appendChild(document.createTextNode(myElementName[1]));
                nodeLink.setAttribute('href', baseTwitchUrl+myElementName);
                nodeLink.innerText = " Visit Channel";
                node.setAttribute("class", "offlineBox");
                node.appendChild(nodeLink);
                document.body.appendChild(node);
            }
            else {
                const myElementName = myArray[i]['_links']['self'].match(/\/streams\/+([a-zA-Z0-9]*)/);
                const node = document.createElement('div');
                node.setAttribute("class", "onlineBox");
                node.appendChild(document.createTextNode(myElementName[1]));
                document.body.appendChild(node);
            }
            asyncTimer(myArray[i], fn); i++;
        }
    };
    fn();
}

letsGo(); // HTML's defer, A script that will not run until after the page has loaded.
