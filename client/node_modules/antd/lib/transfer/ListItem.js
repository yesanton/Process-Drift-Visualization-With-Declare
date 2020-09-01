"use strict";

function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var React = _interopRequireWildcard(require("react"));

var _classnames = _interopRequireDefault(require("classnames"));

var _DeleteOutlined = _interopRequireDefault(require("@ant-design/icons/DeleteOutlined"));

var _default2 = _interopRequireDefault(require("../locale/default"));

var _checkbox = _interopRequireDefault(require("../checkbox"));

var _transButton = _interopRequireDefault(require("../_util/transButton"));

var _LocaleReceiver = _interopRequireDefault(require("../locale-provider/LocaleReceiver"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

function _getRequireWildcardCache() { if (typeof WeakMap !== "function") return null; var cache = new WeakMap(); _getRequireWildcardCache = function _getRequireWildcardCache() { return cache; }; return cache; }

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } if (obj === null || _typeof(obj) !== "object" && typeof obj !== "function") { return { "default": obj }; } var cache = _getRequireWildcardCache(); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj["default"] = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var ListItem = function ListItem(props) {
  var _classNames;

  var renderedText = props.renderedText,
      renderedEl = props.renderedEl,
      item = props.item,
      checked = props.checked,
      disabled = props.disabled,
      prefixCls = props.prefixCls,
      onClick = props.onClick,
      onRemove = props.onRemove,
      showRemove = props.showRemove;
  var className = (0, _classnames["default"])((_classNames = {}, _defineProperty(_classNames, "".concat(prefixCls, "-content-item"), true), _defineProperty(_classNames, "".concat(prefixCls, "-content-item-disabled"), disabled || item.disabled), _defineProperty(_classNames, "".concat(prefixCls, "-content-item-checked"), checked), _classNames));
  var title;

  if (typeof renderedText === 'string' || typeof renderedText === 'number') {
    title = String(renderedText);
  }

  return /*#__PURE__*/React.createElement(_LocaleReceiver["default"], {
    componentName: "Transfer",
    defaultLocale: _default2["default"].Transfer
  }, function (transferLocale) {
    var liProps = {
      className: className,
      title: title
    };
    var labelNode = /*#__PURE__*/React.createElement("span", {
      className: "".concat(prefixCls, "-content-item-text")
    }, renderedEl); // Show remove

    if (showRemove) {
      return /*#__PURE__*/React.createElement("li", liProps, labelNode, /*#__PURE__*/React.createElement(_transButton["default"], {
        disabled: disabled || item.disabled,
        className: "".concat(prefixCls, "-content-item-remove"),
        "aria-label": transferLocale.remove,
        onClick: function onClick() {
          onRemove === null || onRemove === void 0 ? void 0 : onRemove(item);
        }
      }, /*#__PURE__*/React.createElement(_DeleteOutlined["default"], null)));
    } // Default click to select


    liProps.onClick = disabled || item.disabled ? undefined : function () {
      return onClick(item);
    };
    return /*#__PURE__*/React.createElement("li", liProps, /*#__PURE__*/React.createElement(_checkbox["default"], {
      checked: checked,
      disabled: disabled || item.disabled
    }), labelNode);
  });
};

var _default = /*#__PURE__*/React.memo(ListItem);

exports["default"] = _default;