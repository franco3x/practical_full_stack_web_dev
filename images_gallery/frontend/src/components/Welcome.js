import React from 'react';
import Button from 'react-bootstrap/Button';

function Welcome() {
  return (
    <div className="jumbotron">
      <h1>Imagine, Search, Enjoy!</h1>
      <p>Search for something pleighboi!</p>
      <p>
        <Button variant="primary" href="https://unsplash.com" target="_blank">
          Learn more
        </Button>
      </p>
    </div>
  );
}
export default Welcome;
