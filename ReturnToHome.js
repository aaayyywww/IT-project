import React, { useState } from "react";
import "./ReturnToHome.css";
import {Link} from "react-router-dom";
export default function ReturnToHome() {
    const [modal, setModal] = useState(false);

    const toggleModal = () => {
        setModal(!modal);
    };



    return (
        <>
            <button onClick={toggleModal} className="rethomeiconbtn-modal">
                <Link className="link-style" to='/AddOlympiad'>Return to Calendar</Link>
            </button>
        </>
    );
}
