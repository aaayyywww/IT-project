import React, { useState } from "react";
import "./RegisterIcon.css";
import {FaUser} from "react-icons/fa";
import {Link} from "react-router-dom";
export default function RegisterIcon() {
    const [modal, setModal] = useState(false);

    const toggleModal = () => {
        setModal(!modal);
    };



    return (
        <>
            <button onClick={toggleModal} className="regiconbtn-modal">
                <Link to='/UserHome'><FaUser/></Link>
            </button>
        </>
    );
}
