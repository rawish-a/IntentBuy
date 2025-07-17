import React from 'react';
import LoginForm from '../components/LoginForm';
import { loginUser } from '../api/auth';

export default function LoginPage() {
  const handleLogin = async (formData) => {
    try {
      const { access_token } = await loginUser(formData);
      localStorage.setItem('token', access_token);
      alert('Logged in!');
      // Redirect or update UI
    } catch (err) {
      alert(err.message);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10">
      <h1 className="text-xl font-bold mb-4">Login</h1>
      <LoginForm onSubmit={handleLogin} />
    </div>
  );
}
