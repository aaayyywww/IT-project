import React from 'react';
import HorizontalLine from "../funcs/HorizontalLine";
import UserCalendar from "../UserCalendar";
import RegisterIcon from "../funcs/RegisterIcon";
import LogOutButton from "../funcs/LogOutButton";
function AddOlympiad() {


    return (
        <header className="header">
            <div className="container">
                <div className="header-inner">
                    <>
                        <HorizontalLine/>
                        <LogOutButton/>
                        <UserCalendar/>
                        <RegisterIcon/>
                    </>
                </div>
            </div>
        </header>
    );
}

export default AddOlympiad;