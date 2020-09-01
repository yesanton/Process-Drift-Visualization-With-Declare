import InternalRadio from './radio';
import Group from './group';
import Button from './radioButton';
export * from './interface';
var Radio = InternalRadio;
Radio.Button = Button;
Radio.Group = Group;
export { Button, Group };
export default Radio;