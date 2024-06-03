import React from 'react';
import HorizontalLine from "../funcs/HorizontalLine";
import RegisterModal from "../funcs/RegisterModal";
import LoginModal from "../funcs/LogInButton";
import UserCalendar from "../UserCalendar";

function HomePage() {

    return (
        <header className="header">
            <div className="container">
                <div className="header-inner">
                    <>
                        <HorizontalLine/>
                        <RegisterModal/>
                        <LoginModal/>
                        <UserCalendar/>
                    </>
                </div>
            </div>
        </header>
    );
}

export default HomePage;