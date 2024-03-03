use std::time::Instant;
use rand::seq::SliceRandom;

fn merge_sort(mut arr: Vec<i32>, left: usize, right: usize) -> Vec<i32> {
    if right - 1 > left {
        let mid = left + (right - left) / 2;
        arr = merge_sort(arr, left, mid);
        arr = merge_sort(arr, mid, right);
        arr = merge(arr, left, mid, right);
    }
    arr
}


fn merge(mut arr: Vec<i32>, left: usize, mid: usize, right: usize) -> Vec<i32> {
    let n1 = mid - left;
    let n2 = right - mid;
    let l1 = arr.clone();
    let r1 = arr.clone();
    let l = &l1[left..mid];
    let r = &r1[mid..right];
    /* Merge the temp arrays back into arr[l..r]*/
    let mut i = 0; // Initial index of first subarray
    let mut j = 0; // Initial index of second subarray
    let mut k = left; // Initial index of merged subarray
    while i < n1 && j < n2 {
        if l[i] < r[j] {
            arr[k] = l[i];
            i = i + 1;
        } else {
            arr[k] = r[j];
            j = j + 1;
        }
        k = k + 1;
    }
    while i < n1 {
        arr[k] = l[i];
        i = i + 1;
        k = k + 1;
    }
    /* Copy the remaining elements of R[], if there
    are any */
    while j < n2 {
        arr[k] = r[j];
        j = j + 1;
        k = k + 1;
    }
    arr
}

fn main() {
    let now = Instant::now();
    let mut arr: Vec<i32> = (0..1000000).collect();
    let mut rng= rand::thread_rng();
    arr.shuffle(&mut rng);
    merge_sort(arr.clone(), 0, arr.len());
    println!("{}",now.elapsed().as_micros())
}
