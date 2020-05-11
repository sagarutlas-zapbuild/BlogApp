import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import { Link } from 'react-router-dom';
import { TiEdit } from "react-icons/ti";

export const TopNav = (props) => {
    if (props.authenticated) {
        return (<>
            <Navbar collapseOnSelect bg="dark" expand="lg" sticky="top" variant="dark">
                <Navbar.Brand href="#">Blog App</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse className="justify-content-end">

                    <Nav className="mr-auto">
                        <Nav.Item>
                            <Nav.Link as={Link} to="/home">Home</Nav.Link>
                        </Nav.Item>

                        <Nav.Item>
                            <Nav.Link as={Link} to="/me">Hello, {localStorage.getItem('user_name')}
                            </Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link as={Link} to="/createpost"><TiEdit title="New Post" /></Nav.Link>
                        </Nav.Item>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        </>);
    }
    else {
        return (<>
            <Navbar collapseOnSelect bg="dark" expand="lg" sticky="top" variant="dark">
                <Navbar.Brand href="#">Blog App</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse className="justify-content-end">
                    <Nav className="mr-auto">
                        <Nav.Item>
                            <Nav.Link as={Link} to="/home">Home</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link as={Link} to="/login">Login</Nav.Link>
                        </Nav.Item>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        </>);
    }

}
