import React, { useState } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';

function LoginComponent({ onLoginSuccess }) { // Added onLoginSuccess prop
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    const handleLogin = async () => {
        const url = 'http://127.0.0.1:9000/token';
        const data = {
            username: username,
            password: password,
        };

        const config = {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        };

        // Convert data to application/x-www-form-urlencoded format
        const formData = new URLSearchParams();
        formData.append('username', data.username);
        formData.append('password', data.password);

        try {
            const response = await axios.post(url, formData.toString(), config);
            if (response.status === 200) {
                // Assuming the access token and token type are in the response data
                const accessToken = response.data.access_token;
                const tokenType = response.data.token_type;

                // Save the access token and token type in cookies
                Cookies.set('access_token', accessToken, { expires: 30 });
                Cookies.set('token_type', tokenType, { expires: 30 });
                console.log('Successful registration:');
                alert('Registration successful!');

                // Handle successful login
                setIsLoggedIn(true);

                // Call the onLoginSuccess callback function
                if (onLoginSuccess) { // Check if onLoginSuccess is defined
                    onLoginSuccess();
                }
            }
        } catch (error) {
            if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                console.log('Successful failed:');
                alert('Registration failed!');
            } else if (error.request) {
                // The request was made but no response was received
                console.log(error.request);
            } else {
                // Something happened in setting up the request that triggered an Error
                console.log('Error', error.message);
            }
            // Handle error
        }
    };

    const handleLogout = () => {
        Cookies.remove('access_token');
        Cookies.remove('token_type');
        setIsLoggedIn(false);
    };

    return (
        <div>
            <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
            />
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
            />
            {isLoggedIn ? (
                <button type="button" onClick={handleLogout}>
                    Logout
                </button>
            ) : (
                <button type="button" onClick={handleLogin}>
                    Login
                </button>
            )}
        </div>
    );
}

export default LoginComponent;
