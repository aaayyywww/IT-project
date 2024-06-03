import React, { useState } from "react";
import "./RegisterButton.css";
import RegisterForm from "./RegisterForm";

export default function RegisterModal() {
    const [modal, setModal] = useState(false);

    const toggleModal = () => {
        setModal(!modal);
    };

    if(modal) {
        document.body.classList.add('active-modal')
    } else {
        document.body.classList.remove('active-modal')
    }

    return (
        <>
            <button onClick={toggleModal} className="regbtn-modal">
                Sing in
            </button>

            {modal && (
                <div className="regmodal">
                    <div onClick={toggleModal} className="regoverlay"></div>
                    <div className="regmodal-content">
                        <h2>Hello!</h2>
                        <RegisterForm/>
                        <button className="close-modal" onClick={toggleModal}>
                            CLOSE
                        </button>
                    </div>
                </div>
            )}
        </>
    );
}