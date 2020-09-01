import { Tab, TabOffsetMap } from '../interface';
import { TabNavListProps } from '../TabNavList';
export default function useVisibleRange(tabOffsets: TabOffsetMap, containerSize: {
    width: number;
    height: number;
    left: number;
    top: number;
}, { tabs, tabPosition, rtl }: {
    tabs: Tab[];
} & TabNavListProps): [number, number];
