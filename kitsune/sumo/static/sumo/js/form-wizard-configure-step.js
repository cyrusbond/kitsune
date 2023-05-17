import { BaseFormStep } from "sumo/js/form-wizard";
import infoImageURL from "sumo/img/info.svg";
import syncingImageURL from "sumo/img/syncing.svg";
import configureStepStylesURL from "../scss/form-wizard-configure-step.styles.scss";

export class ConfigureStep extends BaseFormStep {
  get template() {
    return `
      <template>
        <div class="configure-step-wrapper">
          <p id="header">
            <img class="icon" src="${infoImageURL}" aria-hidden="true"></img>
            <span>${gettext("You are now logged in to Firefox Accounts")}</span>
            <a href="#" data-event-category="device-migration-wizard" data-event-action="click" data-event-label="forgot-password">${gettext("Forgot password?")}</a>
          </p>
          <p id="sync-status-container">
            <img class="icon" src="${syncingImageURL}" aria-hidden="true"></img>
            <span><strong>${gettext("Syncing:")}</strong></span>
            <span id="sync-status"></span>
          </p>
          <ul id="instructions">
            <li>${gettext("We may not need to say that it’s “off” at the beginning, but rather a “get set up” - type of introduction")}</li>
            <li>${gettext("Make sure there ‘s context for how it works - ex/ timing, frequency, limitations")}</li>
            <li>${gettext("set expectations we sync all data across all devices - can’t pick and choose")}</li>
          </ul>
          <p id="buttons">
            <button id="turn-on-sync" class="mzp-c-button mzp-t-product" data-event-category="device-migration-wizard" data-event-action="click" data-event-label="turn-on-sync">${gettext("Turn on sync")}</button>
            <button id="change-sync-prefs" class="mzp-c-button" data-event-category="device-migration-wizard" data-event-action="click" data-event-label="change-sync-prefs">${gettext("Change what you are syncing")}</button>
            <button id="next" class="mzp-c-button mzp-t-product" data-event-category="device-migration-wizard" data-event-action="click" data-event-label="configuration-next">${gettext("Next")}</button>
          </p>
        </div>
      </template>
    `;
  }

  get styles() {
    let linkEl = document.createElement("link");
    linkEl.rel = "stylesheet";
    linkEl.href = configureStepStylesURL;
    return linkEl;
  }

  connectedCallback() {
    let buttons = this.shadowRoot.querySelector("#buttons");
    buttons.addEventListener("click", this);
  }

  disconnectedCallback() {
    let buttons = this.shadowRoot.querySelector("#buttons");
    buttons.removeEventListener("click", this);
  }

  render(prevState, state) {
    if (this.state.syncEnabled !== prevState.syncEnabled) {
      let statusEl = this.shadowRoot.getElementById("sync-status");
      statusEl.textContent = this.state.syncEnabled
        ? gettext("On")
        : gettext("Off");
      statusEl.toggleAttribute("sync-enabled", this.state.syncEnabled);

      let buttons = this.shadowRoot.getElementById("buttons");
      buttons.toggleAttribute("sync-enabled", this.state.syncEnabled);
      let nextButton = this.shadowRoot.getElementById("next");
      nextButton.disabled = !this.state.syncEnabled;
    }
  }

  handleEvent(event) {
    switch (event.target.id) {
      case "turn-on-sync": {
        this.dispatch("DeviceMigrationWizard:ConfigureStep:TurnOnSync");
        break;
      }
      case "change-sync-prefs": {
        this.dispatch("DeviceMigrationWizard:ConfigureStep:ChangeSyncPrefs");
        break;
      }
      case "next": {
        this.dispatch("DeviceMigrationWizard:ConfigureStep:Next");
        break;
      }
    }
  }

  dispatch(eventName) {
    let event = new CustomEvent(eventName, { bubbles: true });
    this.dispatchEvent(event);
  }
}

customElements.define("configure-step", ConfigureStep);

