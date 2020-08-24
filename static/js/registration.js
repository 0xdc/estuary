register = function(e) {
    e.preventDefault();
    fetch("//localhost:8000/api/registration/begin", {
        method: "GET"
    })
    .then((r) => { if (r.ok) return r.json(); })
    .then(console.log)
}