let token = "2ab5580c215c6cabe52e8358f4b402f2af1d3646"

// Login
async function login(username, password) {
    let formData = new FormData()
    formData.append("username", username)
    formData.append("password", password)


    let response = await fetch("/login/", {
        method: "POST",
        body: formData
    })
    let result = await response.json()
    console.log("Response", result);
}

//Register
async function register(username, password, password_repeat, email, first_name, last_name) {
    let formData = new FormData()
    formData.append("username", username)
    formData.append("password", password)
    formData.append("password_repeat", password_repeat)
    formData.append("email", email)
    formData.append("first_name", first_name)
    formData.append("last_name", last_name)


    let response = await fetch("/register/", {
        method: "POST",
        body: formData
    })
    let result = await response.json()
    console.log("Response", result);
}

async function getChats() {
    let response = await fetch("/chat/get", {
        method: "GET",
        headers: {
            Authorization: token
        }
    })
    let result = await response.json()
    console.log("Response", result);
}

async function getMessages(chat_id) {
    let token = "Token 2ab5580c215c6cabe52e8358f4b402f2af1d3646"
    let response = await fetch("/message/get?chat_id=" + chat_id, {
        method: "GET",
        headers: {
            Authorization: token
        }
    })
    let result = await response.json()
    console.log("Response", result);
}

async function postChat(user_id) {
    let token = "Token 2ab5580c215c6cabe52e8358f4b402f2af1d3646"
    let formData = new FormData()
    formData.append("user_id", user_id)



    let response = await fetch("/board/add/user/", {
        method: "POST",
        headers: {
            Authorization: token
        },
        body: formData
    })
    let result = await response.json()
    console.log("Response", result);
}

async function postMessage(chat_id, message) {
    let token = "Token 2ab5580c215c6cabe52e8358f4b402f2af1d3646"
    let formData = new FormData()
    formData.append("chat_id", chat_id)
    formData.append("text", message)

    let response = await fetch("/message/add", {
        method: "POST",
        headers: {
            Authorization: token
        },
        body: formData
    })
    let result = await response.json()
    console.log("Response", result);

}

async function getUsersWithoutChat() {
    let token = "Token 2ab5580c215c6cabe52e8358f4b402f2af1d3646"
    let response = await fetch("/users/add", {
        method: "GET",
        headers: {
            Authorization: token
        }
    })
    let result = await response.json()
    console.log("Response", result);
}
