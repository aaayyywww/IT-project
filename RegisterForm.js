import {useState} from "react"

const RegisterForm = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [role, setRole] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await fetch('http://127.0.0.1:9000/users/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, email, role, password }),
            });


            if (response.status === 200) {
                // Registration was successful.
                const data = await response.json();
                console.log('Successful registration:', data);
                alert('Registration successful!');


                // You can also display a success message or redirect the user to a different page.

            } else {
                // Registration was not successful.
                const data = await response.json();
                console.log('Successful failed', data);
                alert('Registration failed!');
            }

        } catch (error) {
            // An error occurred during the fetch request or the response status was not 200.
            console.error('Registration failed:', error.message);
            // You can also display an error message to the user.
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Username:
                <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
            </label>
            <label>
                Email:
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
            </label>
            <label>
                Role:
                <input type="text" value={role} onChange={(e) => setRole(e.target.value)} />
            </label>
            <label>
                Password:
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            </label>
            <button type="submit">Register</button>
        </form>
    );
};

export default RegisterForm
