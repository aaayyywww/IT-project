import HomePage from "./pages/Home";
import './App.css';
import {Routes, Route} from "react-router-dom";
import UserCalendar from "./UserCalendar"
import UserHome from "./pages/UserHome";
import AddOlympiad from "./pages/AddOlympiad";

function App() {
    return (
        <>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/usercalendar" element={<UserCalendar/>} />
                <Route path="/UserHome" element={<UserHome/>} />
                <Route path="/AddOlympiad" element={<AddOlympiad/>} />
            </Routes>
        </>
    );
}

export default App;