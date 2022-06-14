import * as tf from "@tensorflow/tfjs";

export class CartPole {
  /**
   * Constructor of CartPole.
   */
  constructor() {
    // Constants that characterize the system.
    this.gravity = 9.8;
    this.massCart = 1.0;
    this.massPole = 0.1;
    this.totalMass = this.massCart + this.massPole;
    this.cartWidth = 0.2;
    this.cartHeight = 0.1;
    this.length = 0.5;
    this.poleMoment = this.massPole * this.length;
    this.forceMag = 10.0;
    this.tau = 0.02; // Seconds between state updates.

    // Threshold values, beyond which a simulation will be marked as failed.
    this.xThreshold = 2.4;
    this.thetaThreshold = (12 / 360) * 2 * Math.PI;

    this.setRandomState();
  }

  /**
   * Set the state of the cart-pole system randomly.
   */
  setRandomState() {
    // The control-theory state variables of the cart-pole system.
    // Cart position, meters.
    this.x = Math.random() - 0.5;
    // Cart velocity.
    this.xDot = (Math.random() - 0.5) * 1;
    // Pole angle, radians.
    this.theta = (Math.random() - 0.5) * 2 * ((6 / 360) * 2 * Math.PI);
    // Pole angle velocity.
    this.thetaDot = (Math.random() - 0.5) * 0.5;
  }

  /**
   * Get current state as a tf.Tensor of shape [1, 4].
   */
  getStateTensor() {
    return tf.tensor2d([[this.x, this.xDot, this.theta, this.thetaDot]]);
  }

  /**
   * Update the cart-pole system using an action.
   * @param {number} action Only the sign of `action` matters.
   *   A value > 0 leads to a rightward force of a fixed magnitude.
   *   A value <= 0 leads to a leftward force of the same fixed magnitude.
   */
  update(action) {
    const force = action > 0 ? this.forceMag : -this.forceMag;

    const cosTheta = Math.cos(this.theta);
    const sinTheta = Math.sin(this.theta);

    const temp =
      (force + this.poleMoment * this.thetaDot * this.thetaDot * sinTheta) /
      this.totalMass;
    const thetaAcc =
      (this.gravity * sinTheta - cosTheta * temp) /
      (this.length *
        (4 / 3 - (this.massPole * cosTheta * cosTheta) / this.totalMass));
    const xAcc =
      temp - (this.poleMoment * thetaAcc * cosTheta) / this.totalMass;

    // Update the four state variables, using Euler's method.
    this.x += this.tau * this.xDot;
    this.xDot += this.tau * xAcc;
    this.theta += this.tau * this.thetaDot;
    this.thetaDot += this.tau * thetaAcc;

    return this.isDone();
  }

  /**
   * Determine whether this simulation is done.
   *
   * A simulation is done when `x` (position of the cart) goes out of bound
   * or when `theta` (angle of the pole) goes out of bound.
   *
   * @returns {bool} Whether the simulation is done.
   */
  isDone() {
    return (
      this.x < -this.xThreshold ||
      this.x > this.xThreshold ||
      this.theta < -this.thetaThreshold ||
      this.theta > this.thetaThreshold
    );
  }
}

/**
 * Render the current state of the system on an HTML canvas.
 *
 * @param {CartPole} cartPole The instance of cart-pole system to render.
 * @param {HTMLCanvasElement} canvas The instance of HTMLCanvasElement on which
 *   the rendering will happen.
 */
export function renderCartPole(cartPole, canvas) {
  if (!canvas.style.display) {
    canvas.style.display = "block";
  }
  const X_MIN = -cartPole.xThreshold;
  const X_MAX = cartPole.xThreshold;
  const xRange = X_MAX - X_MIN;
  const scale = canvas.width / xRange;

  const context = canvas.getContext("2d");
  context.clearRect(0, 0, canvas.width, canvas.height);
  const halfW = canvas.width / 2;

  // Draw the cart.
  const railY = canvas.height * 0.8;
  const cartW = cartPole.cartWidth * scale;
  const cartH = cartPole.cartHeight * scale;

  const cartX = cartPole.x * scale + halfW;

  context.beginPath();
  context.strokeStyle = "#000000";
  context.lineWidth = 2;
  context.rect(cartX - cartW / 2, railY - cartH / 2, cartW, cartH);
  context.stroke();

  // Draw the wheels under the cart.
  const wheelRadius = cartH / 4;
  for (const offsetX of [-1, 1]) {
    context.beginPath();
    context.lineWidth = 2;
    context.arc(
      cartX - (cartW / 4) * offsetX,
      railY + cartH / 2 + wheelRadius,
      wheelRadius,
      0,
      2 * Math.PI
    );
    context.stroke();
  }

  // Draw the pole.
  const angle = cartPole.theta + Math.PI / 2;
  const poleTopX =
    halfW + scale * (cartPole.x + Math.cos(angle) * cartPole.length);
  const poleTopY =
    railY -
    scale * (cartPole.cartHeight / 2 + Math.sin(angle) * cartPole.length);
  context.beginPath();
  context.strokeStyle = "#ffa500";
  context.lineWidth = 6;
  context.moveTo(cartX, railY - cartH / 2);
  context.lineTo(poleTopX, poleTopY);
  context.stroke();

  // Draw the ground.
  const groundY = railY + cartH / 2 + wheelRadius * 2;
  context.beginPath();
  context.strokeStyle = "#000000";
  context.lineWidth = 1;
  context.moveTo(0, groundY);
  context.lineTo(canvas.width, groundY);
  context.stroke();

  const nDivisions = 40;
  for (let i = 0; i < nDivisions; ++i) {
    const x0 = (canvas.width / nDivisions) * i;
    const x1 = x0 + canvas.width / nDivisions / 2;
    const y0 = groundY + canvas.width / nDivisions / 2;
    const y1 = groundY;
    context.beginPath();
    context.moveTo(x0, y0);
    context.lineTo(x1, y1);
    context.stroke();
  }

  // Draw the left and right limits.
  const limitTopY = groundY - canvas.height / 2;
  context.beginPath();
  context.strokeStyle = "#ff0000";
  context.lineWidth = 2;
  context.moveTo(1, groundY);
  context.lineTo(1, limitTopY);
  context.stroke();
  context.beginPath();
  context.moveTo(canvas.width - 1, groundY);
  context.lineTo(canvas.width - 1, limitTopY);
  context.stroke();
}
