import React, { Component } from 'react';
import './UserInput.css';

class UserInput extends Component {
    constructor(props) {
        super(props)
        this.state = {
            menu: "STI",
            kalimat: "",
            hasil: ""
        }
    }
    handleSubmit = (event) => {
        event.preventDefault();
        if (this.state.kalimat !== '') {
            fetch("http://localhost:5000/sundanese-translator", {
                method: "POST",
                headers: { "Content-type": "application/json" },
                body: JSON.stringify({
                    'menu': this.state.menu,
                    'kalimat': this.state.kalimat
                })
            }).then(e => e.json()).then(data => this.setState({ hasil: data.data })).catch((err) => alert("Unvalid sentence :( please make sure each word and character is separated by a whitespace!"))

        } else {
            alert("Your not entering any sentence yet !")
        }
    }

    handleChangeMenu = (event) => {
        event.preventDefault();
        this.setState({
            menu: event.target.value
        });
    }
    handleChangeSentence = (event) => {
        event.preventDefault();
        this.setState({
            kalimat: event.target.value
        })

    }
    render() {
        return (
            <div>
                {/* pilih menu sunda to indonesia ("STI") atau indonesia to sunda ("ITS") */}

                <body className="menu">
                    <br></br>
                    <p className="header-menu"></p>
                    <form>
                        <label>
                            <select className="select-block" onChange={this.handleChangeMenu} >
                                <option value="STI">Sunda-Indonesia</option>
                                <option value="ITS">Indonesia-Sunda</option>
                            </select>
                        </label>
                    </form>

                    {/* masukkan kalimat */}

                    <p className="header-insert-kalimat">Insert Text</p>
                    <form>
                        <input
                            className="num-block"
                            type="text"
                            placeholder="Enter text"
                            onChange={this.handleChangeSentence}
                        />
                    </form>
                    {/* button submit */}
                    <br></br>
                    <div>
                        <button className="submit-button" onClick={this.handleSubmit}>Translate</button>
                    </div>
                    {/* menampilkan hasil terjemahan */}
                    <br></br>
                    <div className="hasil">
                        {this.state.hasil}
                    </div>
                </body>


            </div>
        );
    }
}

export default UserInput;
