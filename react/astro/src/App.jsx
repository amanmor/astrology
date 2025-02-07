import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import NavBar from './components/navigation'
import Home from './components/home'
import About from './components/about'

function App() {

  return (
    <>
        <NavBar></NavBar>
        <Home></Home>
        <About></About>
    </>
  )
}

export default App
