import React, { Component } from 'react';
import './Home.css';
import Footer from './Footer';
import UserInput from './UserInput';
class Home extends Component {
    render() {
        return (
            <div>

                <header className="App-header">
                    {/* <h1>Sorting App</h1>
                    <p className="desc"> helps u sort ur number ! </p> */}
                </header>

                <UserInput />

                <Footer />

            </div>

        );
    }
}

export default Home;