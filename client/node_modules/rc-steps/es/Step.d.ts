import React from 'react';
import { Status, Icons } from './interface';
export interface StepProps {
    prefixCls?: string;
    className?: string;
    style?: React.CSSProperties;
    wrapperStyle?: React.CSSProperties;
    iconPrefix?: string;
    active?: boolean;
    disabled?: boolean;
    stepIndex?: number;
    stepNumber?: number;
    status?: Status;
    title?: React.ReactNode;
    subTitle?: React.ReactNode;
    description?: React.ReactNode;
    tailContent?: React.ReactNode;
    icon?: React.ReactNode;
    icons?: Icons;
    onClick?: React.MouseEventHandler<HTMLDivElement>;
    onStepClick?: (index: number) => void;
    progressDot?: (iconDot: any, info: {
        index: number;
        status: Status;
        title: React.ReactNode;
        description: React.ReactNode;
    }) => React.ReactNode;
}
export default class Step extends React.Component<StepProps> {
    onClick: React.MouseEventHandler<HTMLDivElement>;
    renderIconNode(): any;
    render(): JSX.Element;
}
