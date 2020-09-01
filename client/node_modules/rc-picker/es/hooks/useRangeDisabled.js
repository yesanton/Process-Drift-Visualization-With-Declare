import * as React from 'react';
import { getValue } from '../utils/miscUtil';
import { isSameDate, getQuarter } from '../utils/dateUtil';
export default function useRangeDisabled(_ref) {
  var picker = _ref.picker,
      locale = _ref.locale,
      selectedValue = _ref.selectedValue,
      disabledDate = _ref.disabledDate,
      disabled = _ref.disabled,
      generateConfig = _ref.generateConfig;
  var startDate = getValue(selectedValue, 0);
  var endDate = getValue(selectedValue, 1);
  var disabledStartDate = React.useCallback(function (date) {
    if (disabledDate && disabledDate(date)) {
      return true;
    }

    if (disabled[1] && endDate) {
      return !isSameDate(generateConfig, date, endDate) && generateConfig.isAfter(date, endDate);
    }

    return false;
  }, [disabledDate, disabled[1], endDate]);
  var disableEndDate = React.useCallback(function (date) {
    if (disabledDate && disabledDate(date)) {
      return true;
    }

    if (startDate) {
      if (picker === 'week') {
        var startYear = generateConfig.getYear(startDate);
        var dateYear = generateConfig.getYear(date);
        var startWeek = generateConfig.locale.getWeek(locale.locale, startDate);
        var dateWeek = generateConfig.locale.getWeek(locale.locale, date);
        var startVal = startYear * 100 + startWeek;
        var dateVal = dateYear * 100 + dateWeek;
        return dateVal < startVal;
      }

      if (picker === 'quarter') {
        var _startYear = generateConfig.getYear(startDate);

        var _dateYear = generateConfig.getYear(date);

        var startQuarter = getQuarter(generateConfig, startDate);
        var dateQuarter = getQuarter(generateConfig, date);

        var _startVal = _startYear * 10 + startQuarter;

        var _dateVal = _dateYear * 10 + dateQuarter;

        return _dateVal < _startVal;
      }

      return !isSameDate(generateConfig, date, startDate) && generateConfig.isAfter(startDate, date);
    }

    return false;
  }, [disabledDate, startDate, picker]);
  return [disabledStartDate, disableEndDate];
}