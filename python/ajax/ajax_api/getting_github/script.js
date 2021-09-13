/** @format */

const get_user = async() => {
    var username = document.getElementById("username").value
    await fetch("https://api.github.com/users/" + username)
        .then((res) => res.json())
        .then((data) => build_div(data))
        .catch((err) => console.log(err))
}

const build_div = async(e) => {
    var div = document.createElement("div")
    div.innerHTML = `<h3>${e.login} has ${e.followers} followers</h3><img src="${e.avatar_url}" alt="user_avatar">`
    document.body.appendChild(div)
}