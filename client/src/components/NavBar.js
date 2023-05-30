import React from "react";
import "../styles/NavBar.css";
import { Button, Navbar, Avatar } from "flowbite-react";
import logo from "../images/Quizzy.png";

const NavbarComponent = () => {
  return (
    <Navbar fluid={true} rounded={true}>
      <Navbar.Brand>
      <Avatar
    img={logo}
    size="lg"
  />
        <span className="self-center whitespace-nowrap text-4xl font-semibold dark:text-white">
        Quizzy
        </span>
      </Navbar.Brand>
      <div className="flex 2xl:order-2">
        <Button href="/register" >Get started</Button>
        <Navbar.Toggle  />
      </div>
      <Navbar.Collapse >
        <Navbar.Link href="/" style={{ fontSize: '25px' }}>
          Home
        </Navbar.Link>
        <Navbar.Link href="/scores" style={{ fontSize: '25px' }}>Scores</Navbar.Link>
        <Navbar.Link href="/quiz" style={{ fontSize: '25px' }}>Quiz</Navbar.Link>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default NavbarComponent;
