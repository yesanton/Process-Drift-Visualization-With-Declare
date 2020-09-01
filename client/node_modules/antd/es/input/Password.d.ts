import * as React from 'react';
import { ConfigConsumerProps } from '../config-provider';
import Input, { InputProps } from './Input';
export interface PasswordProps extends InputProps {
    readonly inputPrefixCls?: string;
    readonly action?: string;
    visibilityToggle?: boolean;
    iconRender?: (visible: boolean) => React.ReactNode;
}
export interface PasswordState {
    visible: boolean;
}
export default class Password extends React.Component<PasswordProps, PasswordState> {
    input: HTMLInputElement;
    static defaultProps: {
        action: string;
        visibilityToggle: boolean;
        iconRender: (visible: boolean) => JSX.Element;
    };
    state: PasswordState;
    onVisibleChange: () => void;
    getIcon: (prefixCls: string) => React.FunctionComponentElement<any>;
    saveInput: (instance: Input) => void;
    focus(): void;
    blur(): void;
    select(): void;
    renderPassword: ({ getPrefixCls }: ConfigConsumerProps) => JSX.Element;
    render(): JSX.Element;
}
