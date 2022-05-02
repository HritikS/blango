class ClickButton extends React.Component {
  state = {
    wasClicked: false
  }

  render () {
    return React.createElement(
      'button',
      {
        className: 'btn btn-primary mt-2',
        onClick: () => {
          this.setState(
            {wasClicked: true}
          )
        }
      },
      this.state.wasClicked ? "Clicked!" : "Click Me"
    )
  }
}

ReactDOM.render(
  React.createElement(ClickButton),
  document.getElementById('react_root')
)