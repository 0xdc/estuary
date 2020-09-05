"use strict";

import Gun from 'gun/gun';

var gun = Gun("http://localhost:8765/gun");

document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault()
    var input = document.querySelector("form input");
    gun.get('input').put({message: input.value});
    input.value = '';
})

gun.get('input').on((d,k) => {
    document.querySelector("h1").innerText = d.message;
    document.querySelector("title").innerText = d.message;
})
