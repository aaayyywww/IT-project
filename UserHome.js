import React from 'react';
import HorizontalLine from "../funcs/HorizontalLine";
import RegisterIcon from "../funcs/RegisterIcon";
import UserCalendar from "../UserCalendar";
import ReturnToHome from "../funcs/ReturnToHome";
import LogOutButton from "../funcs/LogOutButton";
function UserHome() {


    return (
        <header className="header">
            <div className="container">
                <div className="header-inner">
                    <>
                        <HorizontalLine/>
                        <LogOutButton/>
                        <RegisterIcon/>
                        <ReturnToHome/>
                        <UserCalendar/>
                    </>
                </div>
            </div>
        </header>
    );
}

export default UserHome;