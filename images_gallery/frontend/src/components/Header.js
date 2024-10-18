import React from 'react';
import { Navbar } from 'react-bootstrap';

const Header = () => {
    return (
        <Navbar bg="light" data-bs-theme="light">
            <Navbar.Brand href="#/">International Image Archive</Navbar.Brand>
        </Navbar>
    )
};

export default Header;