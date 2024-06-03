import React, {Fragment, useState} from "react";
import './LogInButton.css'
import LoginComponent from "./LogIn";
import {Navigate} from "react-router-dom";
import LogOutButton from "./LogOutButton";

export default function LoginModal() {
    const [modal, setModal] = useState(false);
    const [isUserLoggedIn, setIsUserLoggedIn] = useState(false);

    const toggleModal = () => {
        setModal(!modal);
    };

    // Added handleLoginSuccess function
    const handleLoginSuccess = () => {
        toggleModal();
        setIsUserLoggedIn(true);
    };

    return (
        <>
            {isUserLoggedIn ? (
                <Navigate to='/UserHome' />
            ) : (
                <button onClick={toggleModal} className="logbtn-modal">
                    Log in
                </button>
            )}

            {modal && (
                <div className="logmodal">
                    <div onClick={toggleModal} className="logoverlay"></div>
                    <div className="logmodal-content">
                        <h2>Hello!</h2>
                        <LoginComponent onLoginSuccess={handleLoginSuccess} setIsUserLoggedIn={setIsUserLoggedIn} /> {/* Passed setIsUserLoggedIn as a prop */}

                        <button className="close-modal" onClick={toggleModal}>
                            CLOSE
                        </button>
                    </div>
                </div>
            )}
        </>
    );
}
