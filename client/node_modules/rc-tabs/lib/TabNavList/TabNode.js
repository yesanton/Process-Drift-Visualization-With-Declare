"use strict";

var _interopRequireWildcard = require("@babel/runtime/helpers/interopRequireWildcard");

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _defineProperty2 = _interopRequireDefault(require("@babel/runtime/helpers/defineProperty"));

var React = _interopRequireWildcard(require("react"));

var _classnames = _interopRequireDefault(require("classnames"));

var _KeyCode = _interopRequireDefault(require("rc-util/lib/KeyCode"));

function TabNode(_ref, ref) {
  var _classNames;

  var prefixCls = _ref.prefixCls,
      id = _ref.id,
      active = _ref.active,
      rtl = _ref.rtl,
      _ref$tab = _ref.tab,
      key = _ref$tab.key,
      tab = _ref$tab.tab,
      disabled = _ref$tab.disabled,
      closeIcon = _ref$tab.closeIcon,
      tabBarGutter = _ref.tabBarGutter,
      tabPosition = _ref.tabPosition,
      closable = _ref.closable,
      renderWrapper = _ref.renderWrapper,
      removeAriaLabel = _ref.removeAriaLabel,
      editable = _ref.editable,
      onClick = _ref.onClick,
      onRemove = _ref.onRemove,
      onFocus = _ref.onFocus;
  var tabPrefix = "".concat(prefixCls, "-tab");
  React.useEffect(function () {
    return onRemove;
  }, []);
  var nodeStyle = {};

  if (tabPosition === 'top' || tabPosition === 'bottom') {
    nodeStyle[rtl ? 'marginLeft' : 'marginRight'] = tabBarGutter;
  } else {
    nodeStyle.marginBottom = tabBarGutter;
  }

  var removable = editable && closable !== false && !disabled;

  function onRemoveTab(event) {
    event.preventDefault();
    event.stopPropagation();
    editable.onEdit('remove', {
      key: key,
      event: event
    });
  }

  var node = React.createElement("button", {
    key: key,
    ref: ref,
    type: "button",
    role: "tab",
    "aria-selected": active,
    id: id && "".concat(id, "-tab-").concat(key),
    "aria-controls": id && "".concat(id, "-panel-").concat(key),
    tabIndex: 0,
    disabled: disabled,
    className: (0, _classnames.default)(tabPrefix, (_classNames = {}, (0, _defineProperty2.default)(_classNames, "".concat(tabPrefix, "-with-remove"), removable), (0, _defineProperty2.default)(_classNames, "".concat(tabPrefix, "-active"), active), (0, _defineProperty2.default)(_classNames, "".concat(tabPrefix, "-disabled"), disabled), _classNames)),
    onClick: onClick,
    onFocus: onFocus,
    style: nodeStyle
  }, tab, removable && React.createElement("span", {
    role: "button",
    "aria-label": removeAriaLabel || 'remove',
    tabIndex: 0,
    className: "".concat(tabPrefix, "-remove"),
    onClick: function onClick(e) {
      onRemoveTab(e);
    },
    onKeyDown: function onKeyDown(e) {
      if ([_KeyCode.default.SPACE, _KeyCode.default.ENTER].includes(e.which)) {
        onRemoveTab(e);
      }
    }
  }, closeIcon || editable.removeIcon || '×'));

  if (renderWrapper) {
    node = renderWrapper(node);
  }

  return node;
}

var _default = React.forwardRef(TabNode);

exports.default = _default;