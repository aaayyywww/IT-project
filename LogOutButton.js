import React from 'react';
import Cookies from 'js-cookie';
import './LogOutButton.css'
import {useNavigate} from "react-router-dom";
function LogoutButton() {
    const history = useNavigate();
    const handleLogout = () => {
        // Clear the access token and token type cookies
        Cookies.remove('access_token');
        Cookies.remove('token_type');
        history('/')
        // Handle the logout, e.g. redirect to the login page
    };

    return (
        <button type="button" onClick={handleLogout} className="logoutbtn-modal">
            Logout
        </button>
    );
}

export default LogoutButton;